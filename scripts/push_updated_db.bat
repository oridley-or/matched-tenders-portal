@echo off
echo ⏳ Starting DB update and push...

:: Step 1: Copy updated DB file from logic folder
copy "C:\Users\owena\OneDrive\Contract Business June 2025 Build\gov_contracts.db" "C:\Users\owena\OneDrive\matched_tenders_portal\gov_contracts.db" /Y

:: Step 2: Git commit & push
cd "C:\Users\owena\OneDrive\matched_tenders_portal"
git add gov_contracts.db
git commit -m "Automated DB push after contract filtering"
git push

echo ✅ DB push complete — ready to deploy on Render.
exit /b 0
