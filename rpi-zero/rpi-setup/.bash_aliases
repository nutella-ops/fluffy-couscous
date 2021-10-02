for file in $(ls /usr/share/sounds/alsa/Front*wav /usr/share/sounds/alsa/Rear*wav /usr/share/sounds/alsa/Side*wav); do aplay $file; done
