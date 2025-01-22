# Free package for HugeIcons

Check out all 36,000+ hand drawn icons by visiting the HugeIcons website @ https://hugeicons.com/

## Installation

Make sure you have `Django` installed `pip install Django`

After you have installed Django you can install the icon package

`pip install django-hugeicons-stroke`

# Add to your installed apps

Add `django_hugeicons_stroke` under your `installed_apps` variable in your `settings.py` file.

```
INSTALLED_APPS = [
	...
	"django_hugeicons_stroke"
]
```

# Load the template tag per file or globally

If you want to load the icon tag in certain html files just use the following

```
{% load hugeicons_stroke %}
```

or load globally by adding to your `built-ins` in your `TEMPLATES` variable in your `settings.py` file.

```
TEMPLATES = [
    {
		...
        'OPTIONS': {
			...
			'builtins': [
				'django_hugeicons_stroke.templatetags hugeicons_stroke',
            ]
        },
    },
]
```

# Run your server

You're setup and ready to use HugeIcons!

# Using the template tag

```
{% hgi_stroke name="" size="24" color="#000000" stroke_width="2" %}
```

# Parameters

| Name         | Default Value | Description                                   |
| :----------- | :-----------: | :-------------------------------------------- |
| Name         | Empty String  | Name of icon you want to get                  |
| Size         |      24       | The overall size of the icon width and height |
| Color        |    #000000    | `Color text` or `HEX Code` to color the icon  |
| Stroke Width |       2       | The thickness of the icon                     |
