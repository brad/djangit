Djangit
=======

Djangit is a release system built from Django for projects using git as source control.

This is a scratch-my-own-itch project.  I plan on developing it to the point of satisfying my own needs and after that I will be happy to maintain it by fixing small bugs and accepting patches, but I will not be implementing new features unless asked really nicely or paid. ;)

USE
===

Get the source.
```bash
$ cp local_settings.py.example local_settings.py
$ cp local.wsgi.example local.wsgi
```

Tailor these files to your own needs.  The sys.path line is only necessary if you have django projects stored in different locations.  If they are all in the same folder, you can just add a line to the Apache config, as shown below.

Add lines like this to apache conf:
```
WSGIPythonPath /path/to/django/projects/:/usr/lib/python2.6
WSGIScriptAlias /djangit /path/to/djangit/local.wsgi
```

Make a symbolic link to your static files:
```bash
$ sudo ln -s /path/to/djangit/static /var/www/djangit_static
```

Setup a key pair for accessing the server via ssh with no password

Go to /admin and add git branches.  There are two types of branches: beta and release.  The source and target of the Branch object refer the source and target git branch for the release. 

Djangit will ssh to the server and git merge from the specified source branch to the specified target branch, then git pull into the git project branch.  
