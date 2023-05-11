#!/bin/bash

namejob="defaultimportjob"
csvpath="./importjob_default.csv"
while getopts n:p: opt; do
  case $opt in
    n)
      namejob=$OPTARG
      ;;
    p)
      csvpath="./importjob_$OPTARG.csv"
      ;;
    *)
      echo "Bandera no reconocida"
      ;;
  esac
done

poolid="us-west-2_PqrIVeNNd"
arn="arn:aws:iam::180477243137:role/cognito-import-platform-role"
jqversion=$(jq --version)

#Correr el comando para crear el importjob y guardar los resultado en una variable:
importjob=$(aws cognito-idp create-user-import-job --job-name "$namejob" --user-pool-id "$poolid" --cloud-watch-logs-role-arn "$arn")

sleep 1

UserImportJob=`echo ${importjob} | jq -r '.UserImportJob'`

#Obtener el JobId:
JobId=`echo ${UserImportJob} | jq -r '.JobId'`

#Obtener el PreSignedUrl:
PreSignedUrl=`echo ${UserImportJob} | jq -r '.PreSignedUrl'`

tput setaf 2;echo "Se creo el importjob '$namejob' con JobId '$JobId', en la pool '$poolid'"
sleep 1

tput setaf 3;curl=$(curl -v -T "$csvpath" -H "x-amz-server-side-encryption:aws:kms" "$PreSignedUrl")
tput setaf 2;echo "Obteniendo usuarios del csv..."

sleep 1

star=$(aws cognito-idp start-user-import-job --user-pool-id "$poolid" --job-id "$JobId")
tput setaf 2;echo "Iniciando import job..."

sleep 1

sleep 5 &describe=$(aws cognito-idp describe-user-import-job --user-pool-id "$poolid" --job-id "$JobId")
tput setaf 2;echo "Proceso de Descripcion..."
sleep 5
wait $describe

describedata=`echo ${describe} | jq -r '.UserImportJob'`
ImportedUsers=`echo ${describedata} | jq -r '.ImportedUsers'`
SkippedUsers=`echo ${describedata} | jq -r '.SkippedUsers'`
FailedUsers=`echo ${describedata} | jq -r '.FailedUsers'`
CompletionMessage=`echo ${describedata} | jq -r '.CompletionMessage'`
TotalUsers=$((ImportedUsers+FailedUsers+SkippedUsers))

tput setaf 4;echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━IMPORT JOB FINISH━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
tput setaf 4;echo "Al momento de hacer el ImportJob se obtuvo:"
tput setaf 4;echo "Usuarios Importados: $ImportedUsers"
tput setaf 4;echo "Usuarios Skipped: $SkippedUsers"
tput setaf 4;echo "Usuarios Fallidos: $FailedUsers"
tput setaf 4;echo "Total de usuarios: $TotalUsers"
tput setaf 4;echo "Mensaje: $CompletionMessage"