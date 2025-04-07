### 📘 `serverless-installation.md`  
**How to Install Serverless Framework Locally (With SSL Error Fixes)**

---

#### ✅ 1. **Clean Existing Install (Optional but Recommended)**
```powershell
Remove-Item -Recurse -Force .\node_modules\
Remove-Item -Force .\package-lock.json
```

---

#### ✅ 2. **Ensure Node.js and npm Are Installed**
```powershell
node -v
npm -v
```

---

#### ✅ 3. **Fix SSL Issues (Only if You're Behind Corporate Proxy or Facing Cert Errors)**
```powershell
npm config set strict-ssl false
npm config set registry https://registry.npmjs.org/
```

---

#### ✅ 4. **Force TLS 1.2 in PowerShell**
```powershell
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
```

---

#### ✅ 5. **Install Serverless v3 Locally With Offline Plugin**
```powershell
npm install serverless@3 serverless-offline@8.11.0 --save-dev --ignore-scripts --legacy-peer-deps
```
> ⚠️ The `--ignore-scripts` flag skips the post-install fetch that causes SSL certificate errors.
> 
> ⚠️ `serverless-offline@8.11.0` is the last version compatible with Serverless v3.

---

#### ✅ 6. **Bypass TLS Errors When Running Serverless (Development Only)**
```powershell
$env:NODE_TLS_REJECT_UNAUTHORIZED=0
```

---

#### ✅ 7. **Verify Serverless Version**
```powershell
npx serverless --version
```

You should see something like:
```
Serverless ⚡ Framework 3.x.x
```

---

> ✅ You're now ready to use Serverless Framework v3 locally for development.