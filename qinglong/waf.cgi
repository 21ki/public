#!/bin/bash
ngx_conf=/etc/nginx/ip_white.conf
ngx_back=/etc/nginx/ip_white.conf/ip_white.conf.default
printf "Content-Type: text/plain; charset=utf-8\r\n"
printf "\r\n"

printf "ACL white ip list\n"
#echo 'QUERY_STRING:' $QUERY_STRING 
echo 'client:' $REMOTE_ADDR
result=$(cat $ngx_conf |grep $REMOTE_ADDR)
case $REMOTE_ADDR in

rec)
    rm -rf $ngx_conf 
    cp $ngx_back $ngx_conf
     /usr/sbin/nginx -s reload
 ;;

*)
    if [ -z "$result" ]
       then
         echo  "#####add by web #####" >>$ngx_conf
         echo "$REMOTE_ADDR 1;" >> $ngx_conf
         /usr/sbin/nginx -s reload
     else
         exit 0
     fi
;;
esac
