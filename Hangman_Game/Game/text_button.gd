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
	
	var main = get_parent().get_parent()
	var hangman = main.get_node('hangman')
	
#	var w = main.check_win()
#	if w != null:
#		main.lose()
	
	if not text in main.word:
		hangman.show_organ()
		
	else:
		var word = main.word
		word = word.replace(text,"")
		main.word = word
		if word == '':
			main.win()
	
