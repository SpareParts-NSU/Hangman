extends PanelContainer

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
func _input(event):
	if event is InputEventMouseButton:
		var error = get_tree().change_scene('menu.tscn')
		if error != OK:
			print('Error code: {error_code}'.format({'error_code':error}))