%% get File name, and export to excel
% ���ض���׺�����ļ�����ȡ��excel��
% ����cd�����''�е�·��
%
% Xu Yi, 2019

%%
close all; clear; clc;

%%
cd ''; % ���ĵ�ǰ�ļ���
suffix = 'dwf';     % ��Ҫʶ����ļ���ͨ����׺��ʶ��
filename = 'dName.xlsx';     % �������ļ���

mydir = dir(['*.', suffix]); % ��ʶ��.suffix���ļ�
mydirCell = struct2cell(mydir);
mydirNameTemp = mydirCell(1,:); % ��ȡname

mydirName = {0}; DrawNum = {0}; DrawName = {0}; % ��ʼ��
for i = 1:length(mydirNameTemp)
    nameTemp = mydirNameTemp{i};
    nameTemp( end-length(suffix):end ) = []; % ɾ����׺��.suffix
    mydirName{i,1} = nameTemp;
    [DrawNum{i,1}, DrawName{i,1}] = strtok(mydirName{i,1}, '_'); % �ֿ�ͼ����ͼ��
    DrawName{i,1} = DrawName{i,1}(2:end); % ɾ��'_'
end

writecell([mydirName, DrawNum, DrawName],filename); % ����ļ�