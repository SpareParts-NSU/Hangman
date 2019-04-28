extends Control

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

var data_path = 'user://player.data'
var data = {'username':'Guest','password':''}

# Called when the node enters the scene tree for the first time.
func _ready():
	var user = load_data(data_path)
	if user != null:
		print(user)
	#pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_guest_pressed():
	play()
	pass # Replace with function body.


func _on_signup_pressed():
	pass # Replace with function body.


func _on_login_pressed():
	
	pass # Replace with function body.


func play():
	save_data(data_path, data)
	var error = get_tree().change_scene('menu.tscn')
	if error != OK:
		print('Error code: {error_code}'.format({'error_code':error}))

func save_data(path, data):
    var f = File.new()
    f.open(path, File.WRITE)
    f.store_var(data)
    f.close()

func load_data(path):
    var f = File.new()
    if f.file_exists(path):
        f.open(path, File.READ)
        var data = f.get_var()
        f.close()
        return data
    return null