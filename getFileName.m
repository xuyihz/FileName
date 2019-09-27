%% get File name, and export to excel
% 
% 
% 
% Xu Yi, 2019

%%
close all; clear; clc;

%%
suffix = 'dwf';     % 需要识别的文件（通过后缀名识别）
filename = 'dirName.xlsx';     % 导出的文件名

mydir = dir(['*.', suffix]); % 仅识别.suffix的文件
mydirCell = struct2cell(mydir);
mydirNameTemp = mydirCell(1,:); % 提取name

mydirName = {0}; DrawNum = {0}; DrawName = {0}; % 初始化
for i = 1:length(mydirNameTemp)
    mydirName{i,1} = strtok(mydirNameTemp{i},'.'); % 提取文件名中'.'之前的内容，即去掉后缀
    [DrawNum{i,1}, DrawName{i,1}] = strtok(mydirName{i,1}, '_'); % 分开图号与图名
    DrawName{i,1} = DrawName{i,1}(2:end); % 删除'_'
end

writecell([mydirName, DrawNum, DrawName],filename); % 输出文件