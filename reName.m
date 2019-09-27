%% rename Files
%
%
%
% Xu Yi, 2019

%%
close all; clear; clc;

%%
suffix = 'dwf';     % ��Ҫʶ����ļ���ͨ����׺��ʶ��
mydir = dir(['*.', suffix]); % ��ʶ��.suffix���ļ�

for i = 1:length(mydir)
    oldname = files(i).name;
    newname = strcat('RH_', oldname);
    command = ['rename' 32 oldname 32 newname]; % 32 �� ASCII �룬��ʾ�ո�
    status = dos(command); % �����������ִ�в���ϵͳ����
    if status == 0
    else
        disp([oldname, '������ʧ��!\n'])
    end
end