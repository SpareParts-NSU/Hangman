extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

var hits = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	$head.hide()
	$body.hide()
#	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func show_organ():
	var child_count = get_child_count()
	
	if hits < child_count:
		get_child(hits).show()
		hits = hits + 1
	
	if hits == child_count:
		get_parent().lose()