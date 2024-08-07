#!/bin/zsh
asciidoctor -D . **/index.adoc
#rsync -a --verbose --perms --times  --prune-empty-dirs --delete-after doc/images .
#rsync -a --verbose --perms --times  --prune-empty-dirs --delete-after doc/pdf .

