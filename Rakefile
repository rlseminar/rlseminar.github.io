desc "Manage web site publication"

task :serve do
  sh "jekyll serve"
end

task :clean do
  sh "rm -rf _site"
end

task :build do
  sh "jekyll build"
end

task :deploy => [:build] do
  sh "sitecopy --update scan"
end
