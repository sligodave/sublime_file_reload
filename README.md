sublime_file_reload
===================

Sublime Text plugin to reload the current view or all views. Will maintain active views, view orders and groups.


## Installation:


### Git

Clone this repository into your Sublime Text *Packages* directory.

    git clone https://github.com/sligodave/sublime_file_reload.git FileReload


## Configure:

### Settings file:

In the file:

Packages/User/FileReload.sublime-settings

There aren't too many settings. Just a flag to turn on and off printing to the python console.

```json
{
	"debug": false
}
```


## Usage:

### With GoTo Anywhere command:

    "File Reload: Reload all files"
    "File Reload: Reload current file"

### Keyboard shortcuts:

OSX

```json
[
	// Reload the current view
	{ "keys": ["ctrl+super+o", "ctrl+super+o"], "command": "file_reload_reload_view"},
	// Reload all views
	{ "keys": ["ctrl+super+o", "ctrl+super+a"], "command": "file_reload_reload_view", "args": {"all": true}}
]
```

Linux/Windows

```json
[
	// Reload the current view
	{ "keys": ["ctrl+alt+o", "ctrl+alt+o"], "command": "file_reload_reload_view"},
	// Reload all views
	{ "keys": ["ctrl+alt+o", "ctrl+alt+a"], "command": "file_reload_reload_view", "args": {"all": true}}
]
```


## Issues and suggestions:

Fire on any issues or suggestions you have.


## Copyright and license
Copyright 2013 David Higgins

[MIT License](LICENSE)
