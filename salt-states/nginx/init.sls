nginx:
  pkg.installed: []

/etc/nginx/sites-available/default:
  file.absent

kiwidock nginx configuration:
  file.managed:
    - name: '/etc/nginx/conf.d/kiwidock.conf'
    - source: salt://nginx/files/kiwidock.conf

