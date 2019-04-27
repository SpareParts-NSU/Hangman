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
	if not text in get_parent().get_parent().word:
		get_parent().get_parent().get_node('hangman').show_organ()
	else:
		var word = get_parent().get_parent().word
		get_parent().get_parent().word = word.replace(text,"")
		if word == '':
			get_parent().get_parent().win()
