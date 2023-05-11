const b64 = require('base64-js');
const encryptionSdk = require('@aws-crypto/client-node'); 
const DEV="831e7f45-49d8-4ad9-8d12-13bb8dbba372"
const PROD ="9577fa29-85b3-42b6-be0f-b75b5cc0f29c"
const keyaidi =`arn:aws:kms:us-west-2:180477243137:key/${PROD}`
const { encrypt, decrypt } = encryptionSdk.buildClient(encryptionSdk.CommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT);
const generatorKeyId = "arn:aws:kms:us-west-2:180477243137:alias/prod/platform/sso";
const keyIds = [ keyaidi ];
const keyring = new encryptionSdk.KmsKeyringNode({ generatorKeyId, keyIds })

let plainTextCode;
const context = {
    stage: 'demo',
    purpose: 'simple demonstration app',
    origin: 'us-west-2'
  }
const funciones = async () => {
    const { result } = await encrypt(keyring, "926770", { encryptionContext: context });
    console.log(result);
    let base = b64.fromByteArray(result);
    console.log(base);
}
funciones()