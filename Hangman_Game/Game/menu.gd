extends Control



# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _on_quit_pressed():
	get_tree().quit()
	#pass # Replace with function body.


func _on_options_pressed():	
	var error = get_tree().change_scene('options.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))
	#pass # Replace with function body.


func _on_start_pressed():
	var error = get_tree().change_scene('main.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))
	#pass # Replace with function body.
