a = """
<script>
const accessToken = localStorage.getItem('accessToken');
const authorizationHeader = `Bearer ${accessToken}`;
const originalOpen = XMLHttpRequest.prototype.open;
XMLHttpRequest.prototype.open = function(method, url, async) {
this.requestUrl = url;
return originalOpen.apply(this, arguments);
};
(function(send) {
XMLHttpRequest.prototype.send = function(data) {
let isPlatformUrl = this.requestUrl.indexOf('platform') != -1;
if (accessToken && isPlatformUrl) {
this.setRequestHeader('Authorization', `Bearer ${accessToken}`);
}
send.call(this, data);
};
})(XMLHttpRequest.prototype.send);
const originalFetch = window.fetch;
window.fetch = function() {
for (let len = arguments.length, args = Array(len), key = 0; key < len; key++) {
args[key] = arguments[key];
}
const resource = args[0];
let config = args[1];
let isPlatformUrl = resource.indexOf('platform') != -1;
if (accessToken && isPlatformUrl) {
if (!config.headers) {
config.headers = {};
}
config.headers['Authorization'] = authorizationHeader;
}
return originalFetch(resource, config);
};
</script>
"""
b= """
<script>
const accessToken = localStorage.getItem('accessToken');
const authorizationHeader = `Bearer ${accessToken}`;
const originalOpen = XMLHttpRequest.prototype.open;
XMLHttpRequest.prototype.open = function(method, url, async) {
this.requestUrl = url;
return originalOpen.apply(this, arguments);
};
(function(send) {
XMLHttpRequest.prototype.send = function(data) {
let isPlatformUrl = this.requestUrl.indexOf('platform') != -1;
if (accessToken && isPlatformUrl) {
this.setRequestHeader('Authorization', `Bearer ${accessToken}`);
}
send.call(this, data);
};
})(XMLHttpRequest.prototype.send);
const originalFetch = window.fetch;
window.fetch = function() {
for (let len = arguments.length, args = Array(len), key = 0; key < len; key++) {
args[key] = arguments[key];
}
const resource = args[0];
let config = args[1];
let isPlatformUrl = resource.indexOf('platform') != -1;
if (accessToken && isPlatformUrl) {
if (!config.headers) {
config.headers = {};
}
config.headers['Authorization'] = authorizationHeader;
}
return originalFetch(resource, config);
};
</script>
"""
print(a==b)