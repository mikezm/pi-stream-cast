#!/bin/bash

BRANCH=$1

APACHE_HOST_DIR=/usr/local/var/www/risk-monitor.com
REPO_DIR=/Users/mike/bin/risk-monitor
REPO_API_DIR=/Users/mike/bin/risk-monitor/server/src
WSGI_FILE=/Users/mike/.private/api.wsgi

if [[ -z $BRANCH ]]; then
  BRANCH="main"
fi

checkout_branch()
{
  cd $REPO_DIR || exit
  git pull --rebase
  git checkout $BRANCH
}

prep_apache_dir()
{
  echo "prepping apache host directory"
  cd $APACHE_HOST_DIR || exit
  rm -Rf ./*
  mkdir ./api
}

build_and_install_site()
{
  echo "running site build"
  cd "$REPO_DIR/www" || exit
  rm -Rf ./build/*
  npm install
  npm run build
  cp -Rf ./build/* "$APACHE_HOST_DIR/"
}

install_api()
{
  echo "installing API"
  cd "$REPO_DIR/server/src" || exit
  cp ./application.py "$APACHE_HOST_DIR/api/"
  cp -R ./app "$APACHE_HOST_DIR/api/"
  cp $WSGI_FILE "$APACHE_HOST_DIR/api/"
}

restart_apache()
{
  echo "restarting apache"
  brew services restart httpd
}

# Main
checkout_branch
prep_apache_dir
build_and_install_site
install_api
restart_apache
exit 0