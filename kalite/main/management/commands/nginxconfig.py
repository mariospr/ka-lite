"""
"""
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


config_template = """

    # This file is generated by KA-Lite optimizerpi.sh: do not edit
    #
    # Upstream KA-Lite server is normally port 7007
    # Nginx proxy for KA-Lite is normally port 8008
    #
    # If you want the website to be accessible at a different port, add
    #  a PROXY_PORT = nnnn setting in ka-lite/local_settings.py
    # If you need to run the KA-Lite cherrypyserver on a different port,
    #  add a PRODUCTION_PORT = nnnn setting in ka-lite/local_settings.py
    #
    # IMPORTANT: after changing the local_settings.py
    #    execute ./scripts/optimizerpi.sh to regenerate this configuration


upstream kalite {
    server 127.0.0.1:%(production_port)s;
}

server {

    listen %(proxy_port)s;

    location /static {
        alias   %(root_path)s/kalite/static/;
    }

    location /media {
        alias   %(root_path)s/kalite/media/;
    }

    location /content {
        alias   %(root_path)s/content/;
    }

    location /favicon.ico {
        empty_gif;
    }

    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass http://kalite;
        error_page 502 = @502;
    }

    location @502 {
        types { }
        default_type "text/html";
        return 502 "
        <BR>
        <H1>KA-Lite might be busy - wait a few moments and then reload this page
        <BR><BR>
        <H2>If KA-Lite is still busy, get help from the system administrator
        <H3>Error code: nginx 502 Bad Gateway (maybe the KA-Lite webserver is not working correctly)";
    }

}

"""

class Command(BaseCommand):
    help = "Print recommended Nginx frontend proxy configuration file contents."

    def handle(self, *args, **options):
        self.stdout.write(config_template % {"root_path": os.path.realpath(settings.PROJECT_PATH + "/../"),
                                             "production_port": settings.PRODUCTION_PORT,
                                             "proxy_port": settings.PROXY_PORT})


