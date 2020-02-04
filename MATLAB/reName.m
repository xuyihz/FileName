%% rename Files
% filename = 'dName.xlsx' ������ļ����в������ļ���׺��
% ��������ĺ�׺��, ����system('rename *.oldSuffix *.newSuffix')
% ����cd�����''�е�·��
% Xu Yi, 2019

%%
close all; clear; clc;

%%
cd ''; % ���ĵ�ǰ�ļ���
oldSuffix = 'dwf';     % Դ�ļ���׺��
newSuffix = 'dwf';     % ��Ҫ���ĺ�ĺ�׺��
filename = 'dName.xlsx';     % ��ȡ���ļ���

mydir = dir(['*.', oldSuffix]); % ��ʶ��.oldSuffix���ļ�
mydirCell = struct2cell(mydir);
oldName = mydirCell(1,:); % ��ȡname
newName = readcell(filename);
for i = 1:length(mydir)
    command = ['rename', ' "', oldName{i}, '" "',...
        newName{i,1}, '.', newSuffix, '"'];
    % rename [<Drive>:][<Path>]<FileName1> <FileName2>
    % �ļ������пո�ʱ����Ҫ��·�����""
    status = system(command); % �����������ִ�в���ϵͳ����
    if status ~= 0
        disp([oldName{i}, '������ʧ�ܡ�\n'])
    end
end