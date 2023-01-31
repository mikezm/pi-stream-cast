#!/bin/bash

BRANCH=$1

APACHE_HOST_DIR=/var/www/html/pi-stream-cast
REPO_DIR=/home/mike/bin/pi-stream-cast
REPO_API_DIR="$REPO_DIR/server"

if [[ -z $BRANCH ]]; then
  BRANCH="main"
fi

checkout_branch()
{
  cd $REPO_DIR || exit
  git pull --rebase || exit
  git checkout $BRANCH || exit
}

prep_apache_dir()
{
  echo "prepping apache host directory"
  sudo rm -Rf "$APACHE_HOST_DIR/*"
  sudo mkdir "$APACHE_HOST_DIR/api"
  sudo chown -Rf www-data:www-data "$APACHE_HOST_DIR/api"
}

build_and_install_site()
{
  echo "running site build"
  cd "$REPO_DIR/www" || exit
  rm -Rf ./build/*
  npm install
  npm run build
  sudo cp -Rf ./build/* "$APACHE_HOST_DIR/"
  sudo chown -Rf www-data:www-data "$APACHE_HOST_DIR/*"
}

install_api()
{
  echo "installing API"
  cd "$REPO_DIR/server/" || exit
  sudo cp ./{application.py,api.wsgi} "$APACHE_HOST_DIR/api/"
  sudo cp -R ./app "$APACHE_HOST_DIR/api/"
  sudo chown -Rf www-data:www-data "$APACHE_HOST_DIR/*"
}

restart_apache()
{
  echo "restarting apache"
  sudo systemctl restart apache2 
}

# Main
checkout_branch
prep_apache_dir
build_and_install_site
install_api
restart_apache
exit 0