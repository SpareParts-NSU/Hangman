extends Control

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

var file_path = 'user://player.data'
var file_data = {'username':'Guest'}

const GET_DATA = preload('res://get_data.tscn')
const POST_DATA = preload('res://post_data.tscn')

# Called when the node enters the scene tree for the first time.
func _ready():
	$warning.hide()
	global.username = ''
	var user = load_data(file_path)
	if user != null:
		play()
#	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_guest_pressed():
	save_data(file_path, file_data)
	play()
	pass # Replace with function body.


func _on_signup_pressed():
	var username = $v_box_container/username.get_text()
	var password = $v_box_container/password.get_text().sha256_text()
	var email = $v_box_container/email.get_text()
	
	if username == '':
		$warning/label.set_text("Please enter a valid username")
		$warning.show()
		yield(get_tree().create_timer(0.5),"timeout")
		$warning.hide()
		return

	if email == '':
		$warning/label.set_text("Please enter a valid email address")
		$warning.show()
		yield(get_tree().create_timer(0.5),"timeout")
		$warning.hide()
		return

	if password == '' or password.length() < 8:
		$warning/label.set_text("Please enter a password of at least 8 characters")
		$warning.show()
		yield(get_tree().create_timer(0.5),"timeout")
		$warning.hide()
		return
	
	if(signup(username, password, email) == null):
		$warning/label.set_text("Username/Email already taken!")
		$warning.show()
		yield(get_tree().create_timer(0.5),"timeout")
		$warning.hide()
		return
	
	file_data['username'] = username
	save_data(file_path, file_data)
	play()
	
	pass # Replace with function body.


func _on_login_pressed():
	var username = $v_box_container/username.get_text()
	var password = $v_box_container/password.get_text().sha256_text()
	
	if username == '':
		$warning/label.set_text("Please enter your username")
		$warning.show()
		yield(get_tree().create_timer(1),"timeout")
		$warning.hide()
		return

	if password == '' or password.length() < 8:
		$warning/label.set_text("Please enter your password")
		$warning.show()
		yield(get_tree().create_timer(1),"timeout")
		$warning.hide()
		return
	
	login(username, password)
	
#	pass # Replace with function body.


func signup(username, password, email):
	
	var post_data = POST_DATA.instance()
	
	var body = {"avatar" : null, "alias" : username, "email" : email, "password" : password}
	body = to_json(body)
	
	post_data.http_connect()
	
	var data = post_data.post_data("/user/", body)
	
	return data


func login(username, password):
	
	var get_data = GET_DATA.instance()
	get_data.http_connect()
	var info = parse_json(get_data.get_data('/user/' + username + "/"))
	
	if info == null:
		$warning/label.set_text("The username does not exist")
		$warning.show()
		yield(get_tree().create_timer(1),"timeout")
		$warning.hide()
		return
	
	elif password != info["password"]:
		$warning/label.set_text("Incorrect password!")
		$warning.show()
		yield(get_tree().create_timer(1),"timeout")
		$warning.hide()
		return
	
	file_data['username'] = username
	save_data(file_path, file_data)
	play()


func play():
	global.username = file_data['username']
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
