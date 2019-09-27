%% rename Files
%
%
%
% Xu Yi, 2019

%%
close all; clear; clc;

%%
suffix = 'dwf';     % 需要识别的文件（通过后缀名识别）
mydir = dir(['*.', suffix]); % 仅识别.suffix的文件

for i = 1:length(mydir)
    oldname = files(i).name;
    newname = strcat('RH_', oldname);
    command = ['rename' 32 oldname 32 newname]; % 32 是 ASCII 码，表示空格。
    status = dos(command); % 这个函数调用执行操作系统命令
    if status == 0
    else
        disp([oldname, '重命名失败!\n'])
    end
end