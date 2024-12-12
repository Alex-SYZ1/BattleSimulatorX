import configparser,re,sys,os
"""用于导入项目中不在同一文件夹的库"""
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from collections import defaultdict
from utils import constants

def read_init_file():
    filename = "data/parameter.ini"
    config = configparser.ConfigParser()
    config.read(filename, encoding="utf-8")

    config_data = {}
    for section in config.sections():
        config_data[section] = {}
        for key in config[section]:
            value = config[section][key]

            # 若为身份证号，保留为字符串即可
            if re.match(r'^\d{17}[\dXx]$', value):
                pass
            elif value.lower() in ["true", "false"]:
                value = config.getboolean(section, key)
            elif value.isdigit():
                value = config.getint(section, key)
            else:
                try:
                    value = config.getfloat(section, key)
                except ValueError:
                    pass

            config_data[section][key] = value

    return config_data

get_user_info_dict   = lambda config_data:config_data["user"]
get_person_info_list = lambda config_data:[config_data[i] for i in config_data if i.startswith("person")] 
get_alert_locator    = lambda alert_text:constants.VisitorPage3_alert_xpath.format(alert_text=alert_text)
get_time_info_dict   = lambda config_data:config_data["wait_time"]
get_recipient_info_dict = lambda config_data:[config_data[i] for i in config_data if i.startswith("recipient")]


def get_email_info_dict(config_data):
    recipient_info = get_recipient_info_dict(config_data)
    initial_email_info_dict = {i:j  for i,j in (config_data["email"]).items()}
    if initial_email_info_dict["intime_inform"]:
        three_dates = '第一天 第二天 第三天'.split()
        update2recipient = defaultdict(list)
        for recipient in recipient_info:
            chosen_dates = [three_dates.index(i) for i in recipient["inform_update"].split()]
            for update_index in chosen_dates:
                update2recipient[update_index].append(recipient["recipient_email"])
        initial_email_info_dict["update2recipient"] = update2recipient
        # print(initial_email_info_dict)
        # input("********************************")
    return initial_email_info_dict
    #else:return 
        
def get_file_txt(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        txt = f.read()
    return txt

class Person:
    def __init__(self, Person_info: dict):
        self._name = Person_info["person_name"]
        self._idnumber = Person_info["person_idnumber"]
        self._phone = Person_info["person_phone"]
        self._reason = Person_info["person_reason"]
        self._date = Person_info["person_date"]
        self._time = Person_info["person_time"]
        self._gate = Person_info["person_gate"]
        self._phoneIndex = 1

    def to_json(self):
        return self.__dict__#json.dumps(self.__dict__, ensure_ascii=False)

if __name__ == "__main__":
    UserInitProfiles = read_init_file()
    print(UserInitProfiles)
    print(Person(get_person_info_list(UserInitProfiles)[0]).to_json())
    