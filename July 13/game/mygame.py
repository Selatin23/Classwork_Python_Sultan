import json
import  time

quest_filename = 'story.json'
with open (quest_filename, encoding='utf-8') as quest_file:
    quest = json.load(quest_file)

current_scene = "SCENE_0"

def show_description(scene):
    print(quest["SCENES"][current_scene]["DESCRIPTION"])

def show_actions(scene):
    print("\nЧто будем делать?")
    for action in quest["SCENES"][current_scene]["ACTIONS"]:
        print(" -> ", action ["NAME"])

def ger_action_effect(scene, action_name):
    for a in quest["SCENES"][scene]["AACTIONS"]:
        if action_name == a["NAME"]:
            return a["EFFECT"]

while True:
    time.sleep(2)
    show_description(current_scene)
    show_actions(current_scene)
    action = input()
    effect = get_action_effect(current_scene, action)
    if not effect:
        print("Не возможно такое действие!")
        continue

