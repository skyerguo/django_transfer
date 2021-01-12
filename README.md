# django_transfer

# server
    ```
        cd ~/distComuputing
        python manage.py migrate
        python manage.py runserver --ipv6 [::]:8000
    ```
# client
    ```
        cd ~/client
        cpulimit -l 50 python main.py
    ```