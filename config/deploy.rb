# config valid only for current version of Capistrano
lock "3.11.0"

set :application, "nanonets"
set :branch, "master"
set :repo_url, "git@github.com:Prashant31/nn_assignment.git"

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, "/var/www/my_app_name"

# Default value for :format is :airbrussh.
# set :format, :airbrussh

# You can configure the Airbrussh format using :format_options.
# These are the defaults.
# set :format_options, command_output: true, log_file: "log/capistrano.log", color: :auto, truncate: :auto

# Default value for :pty is false
set :pty, true
set :tld, "ec2-3-19-53-243.us-east-2.compute.amazonaws.com"
set :user, "ubuntu"
# Default value for :linked_files is []
# append :linked_files, "config/database.yml", "config/secrets.yml"

# Default value for linked_dirs is []
# append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "public/system"

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for keep_releases is 5
set :keep_releases, 3

namespace :deploy do
  after "deploy:install", "nginx:install"
  after "nginx:install", "supervisor:setup"

  after "deploy:published", "deploy:refresh"
  after "deploy:finished", "django:setup"
  after "django:setup", "mysql:restart"
  after "mysql:restart", "supervisor:services_restart"
  after "supervisor:services_restart", "nginx:restart"
end
