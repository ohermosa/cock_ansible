export OS_AUTH_URL=http://asgard.es.datio:15000/v3/
export OS_PROJECT_ID=d0f3b28924d4414d9ac36c0224131d65
export OS_PROJECT_NAME="cop-ansible"
export OS_USER_DOMAIN_NAME="operations"
export OS_USERNAME="ohermosa"
echo "Please enter your OpenStack Password for project $OS_PROJECT_NAME as user $OS_USERNAME: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT
