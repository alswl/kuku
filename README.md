#kuku#

Online Image Manager based on web.py, a weekend project.

#Install#

## uwsgi ##

```
[uwsgi]
socket = /socket/path/uwsgi_kuku.sock
chmod-socket = 660
virtualenv = /virtualenvs/path/.virtualenvs/kuku/
chdir = /project/path/
wsgi-file = kuku.py
daemonize=/log/path/uwsgi_kuku.log

listern = 20
process = 4
limit-as = 256
harakiri = 60
```

## nginx ##

```
server {
    listen       80;
    server_name  your.domain;

        location ^~ /static/ {
                root /project/path/;
                expires 30d;
                access_log off;
        }

        location ^~ /upload/ {
                root /project/path/;
                access_log off;
        }

    location /{
        include uwsgi_params;
        uwsgi_pass unix:/socket/path/uwsgi_kuku.sock;
    }
}

# vim: set ft=nginx:
```

Thanks to [web.py][] / [Foundation][] / [cdnjs][] / [Google Hosted Libraries][]

[web.py]: http://webpy.org/
[Foundation]: http://foundation.zurb.com/
[cdnjs]: http://cdnjs.com
[Google Hosted Libraries]: https://developers.google.com/speed/libraries/
