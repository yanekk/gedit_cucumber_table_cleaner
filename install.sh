#!/bin/sh
if [ ! -d $HOME/.gnome2/gedit/plugins ]
then
  mkdir -p ~/.gnome2/gedit/plugins
fi
cp -R lib/* ~/.gnome2/gedit/plugins

