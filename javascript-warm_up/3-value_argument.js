#!/usr/bin/node

const { argv } = require('node:process');

// print process.argv
argv.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});
if not argv console.log("No argument")