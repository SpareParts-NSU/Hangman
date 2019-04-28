extends Control

var file_path = 'user://player.data'

# Called when the node enters the scene tree for the first time.
func _ready():
	var user = load_data(file_path)
	$label.set_text("Hello " + user["username"])
#	pass # Replace with function body.


func _on_quit_pressed():
	get_tree().quit()
	#pass # Replace with function body.


func _on_options_pressed():	
	var error = get_tree().change_scene('options.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))
	#pass # Replace with function body.


func _on_singleplayer_pressed():
	var error = get_tree().change_scene('single_player.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))
	#pass # Replace with function body.


func _on_multiplayer_pressed():
	var error = get_tree().change_scene('multi_player.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))
	#pass # Replace with function body.


func _on_login_pressed():
	var f = File.new()
	f.open('user://player.data', File.WRITE)
	f.close()
	var error = get_tree().change_scene('login.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))
#	pass # Replace with function body.

func load_data(path):
    var f = File.new()
    if f.file_exists(path):
        f.open(path, File.READ)
        var data = f.get_var()
        f.close()
        return data
    return null
