nginx:
  pkg.installed: []

/etc/nginx/sites-available/default:
  file.absent

kiwidock nginx configuration:
  file.managed:
    - name: '/etc/nginx/conf.d/kiwidock.conf'
    - source: salt://nginx/files/kiwidock.conf

localhost.crt:
  file.managed:
    - name: '/etc/nginx/ssl/localhost.crt'
    - source: salt://nginx/files/localhost.crt
    - makedirs: True

localhost.key:
  file.managed:
    - name: '/etc/nginx/ssl/localhost.key'
    - source: salt://nginx/files/localhost.key
    - makedirs: True

