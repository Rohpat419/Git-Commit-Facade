# make the entire workflow configurable



# allow the user to run this script which will replace the current config.yml

import sys
import argparse
import shutil
import os

description_msg = "This script replaces the github workflow's current config with a config file from the templates/ dir."

help_msg = "Show this message and exit"

f_msg = "Supply the file name from the templates/ dir whose configuration you want to apply to the github workflow. e.g cron_config.py -f oneADay.yml"

username_msg = "Please enter your github username so that it can be entered into the github action config."

email_msg = "Please enter your github email so that it can be entered into the github action config."


def file_entered(argFileName):
    if not (argFileName.endswith(".yaml") or argFileName.endswith(".yml")):
        argFileName += ".yml"
        
    print(argFileName)
    file_name = argFileName
    new_cfg = "templates/" + file_name
    print(new_cfg)
    
    try: 
        target_dir = ".github/workflows/"
        target_file = "newcfg.yml"
        full_path = target_dir+target_file
        shutil.copy(new_cfg, full_path)
        # if the copy was successful then we can also clear anything else from that dir
        if os.path.exists(full_path):
            print("File copied successfully, clearing up the rest of the directory")
            
            for file in os.listdir(target_dir):
                delete_file_path = os.path.join(target_dir, file)
                if delete_file_path != full_path and os.path.isfile(delete_file_path):
                    os.remove(delete_file_path)
        else:
            print("Could not verify that the file was copied. Did not perform any cleanup of the .github/workflows directory, please perform a manual inspection of that dir.")
        # And now I want to rename it to config.yml because it feels cleaner
        os.rename(full_path, target_dir+"config.yml")
        
    except FileNotFoundError as e:
        print("Could not find the following file in the templates dir: " + file_name)
        
    except Exception as e: 
        print("An error occured:", Exception)
    
    return

# open the config file, and replace the user.name with the entered username
def replace_username(username):
    config_path = ".github/workflows/config.yml"
    with open(config_path, 'r') as config_file:
        content = config_file.read()
    
    updated_content = content.replace("your-github-username", username)
    
    with open(config_path, 'w') as config_file: 
        config_file.write(updated_content)
    return

def replace_email(email):
    config_path = ".github/workflows/config.yml"
    with open(config_path, 'r') as config_file: 
        content = config_file.read()
    
    updated_content = content.replace("your-email", email)
    
    with open(config_path, 'w') as config_file:
        config_file.write(updated_content)
    
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description_msg)
    # parser.add_argument('-h', '--help', action='help', help=help_msg)
    # print("To use the cron config script ")
    parser.add_argument('-f', '--file', help=f_msg)
    parser.add_argument('-u', '--username', help=username_msg, required=True)
    parser.add_argument('-e', '--email', help=email_msg, required=True)
    args = parser.parse_args()
    
    
    # user chose to enter a template filename as input
    if args.file:
        file_entered(args.file)
        replace_username(args.username)
        replace_email(args.email)

    

