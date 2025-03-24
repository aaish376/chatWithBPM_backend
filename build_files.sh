{ 
"version": 2, 
"builds": [ 
{ 
"src": "ChatWithBPMBackend/wsgi.py", 
"use": "@vercel/python", 
You, 57 minutes ago added vercel 
"config": { "maxLambdaSize": "15mb", "runtime": "python3.9" } 
}, 
{ 
"src": "build_files.sh", 
"use": "@vercel/static-build", 
"config": { 
"distDir": "staticfiles_build" 
} 

], 
"routes":[ 
{ 
"src": "/static/(.*)", 
"dest": "/static/$1" 
}, 
{ 
"src": "/(.*)", 
"dest": "ChatWithBPMBackend/wsgi.py" 
} 
}