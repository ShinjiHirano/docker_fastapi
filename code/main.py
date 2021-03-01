from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import ckan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def hello():
    return { "text": "hello, docker Python world!" }

@app.get('/group_list')
async def group_list(
    url: str):
    return ckan.group_list(url)

@app.get('/organization_list')
async def organization_list(
    url: str):
    return ckan.organization_list(url)

@app.get('/organization_show')
async def organization_show(
    url: str,
    organization: str):
    return ckan.organization_show(url, organization)

@app.get('/tag_list')
async def tag_list(
    url: str):
    return ckan.tag_list(url)

@app.get('/package_search')
async def package_search(
    url: str, organization: str):
    return ckan.package_search(url, organization)

@app.get('/download_resource')
async def download_resource(
    url: str,
    res_url: str):
    return ckan.download_resource(url, res_url)

