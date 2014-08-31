#!/bin/bash
for localedir in ./balin/*/locale; do
    app_dir="$(dirname $localedir)"
    echo "Entering ${app_dir}..."
    cd "$app_dir" && django-admin.py makemessages -l pt_BR "$@" && cd - > /dev/null
    echo '----'
done
