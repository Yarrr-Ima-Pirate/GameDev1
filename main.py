
import unreal

levelTools = unreal.Level
editorlevelLibrary = unreal.EditorLevelLibrary
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

#init new level
newLevel = "myNewLevel"

#create Kick ass new Level the likes of which you have never seen
myNewLevel = levelSubSys.new_level("/Game/Levels/newLevel")

#Set level as current level
levelSubSys.set_current_level_by_name(newLevel)

#save level
levelSubSys.save_current_level()