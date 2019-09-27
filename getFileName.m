%% get File name, and export to excel
% 
% 
% 
% Xu Yi, 2019

%%
close all; clear; clc;

%%
suffix = 'dwf';     % ��Ҫʶ����ļ���ͨ����׺��ʶ��
filename = 'dirName.xlsx';     % �������ļ���

mydir = dir(['*.', suffix]); % ��ʶ��.suffix���ļ�
mydirCell = struct2cell(mydir);
mydirNameTemp = mydirCell(1,:); % ��ȡname

mydirName = {0}; DrawNum = {0}; DrawName = {0}; % ��ʼ��
for i = 1:length(mydirNameTemp)
    mydirName{i,1} = strtok(mydirNameTemp{i},'.'); % ��ȡ�ļ�����'.'֮ǰ�����ݣ���ȥ����׺
    [DrawNum{i,1}, DrawName{i,1}] = strtok(mydirName{i,1}, '_'); % �ֿ�ͼ����ͼ��
    DrawName{i,1} = DrawName{i,1}(2:end); % ɾ��'_'
end

writecell([mydirName, DrawNum, DrawName],filename); % ����ļ�