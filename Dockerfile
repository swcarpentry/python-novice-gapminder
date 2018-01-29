FROM jekyll/jekyll:3

RUN apk add -q --no-cache python3 make
COPY . /srv/jekyll
RUN chmod -R a+rX,g+rwX /srv/jekyll && chown -R jekyll: /srv/jekyll
