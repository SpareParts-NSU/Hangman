extends Button

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass
#	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func _pressed():
	print(self.text)
	disabled = true
	get_parent().get_parent().get_node('letter_container').get_node(text).text = text
	get_parent().get_parent().word = get_parent().get_parent().word.replace(text,"")
