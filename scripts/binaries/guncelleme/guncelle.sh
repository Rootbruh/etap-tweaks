#!/bin/bash
brand="Pardus ETAP"

if [ "$(id -nu)" != "root" ]; then
    while :; do
        sudo -k
        pass=$(whiptail --backtitle "$brand Güncelleyici" --title "Yetki Gerekli" --passwordbox "$USER: kullanıcısı için parola giriniz." 12 50 3>&2 2>&1 1>&3-)
        echo $pass | sudo -S apt install ./paketler/*.deb -yq
        if [ "$?" = "0" ]; then
            /bin/sh /usr/bin/eta-restart-shell.sh
            break
        fi
    done
    exit 1
fi
