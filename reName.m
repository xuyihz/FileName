%% rename Files
% filename = 'dName.xlsx' 这里的文件名中不包含文件后缀名
% 如需仅更改后缀名, 运行system('rename *.oldSuffix *.newSuffix')
% 更改cd命令后''中的路径
% Xu Yi, 2019

%%
close all; clear; clc;

%%
cd ''; % 更改当前文件夹
oldSuffix = 'dwf';     % 源文件后缀名
newSuffix = 'dwf';     % 需要更改后的后缀名
filename = 'dName.xlsx';     % 读取的文件名

mydir = dir(['*.', oldSuffix]); % 仅识别.oldSuffix的文件
mydirCell = struct2cell(mydir);
oldName = mydirCell(1,:); % 提取name
newName = readcell(filename);
for i = 1:length(mydir)
    command = ['rename', ' "', oldName{i}, '" "',...
        newName{i,1}, '.', newSuffix, '"'];
    % rename [<Drive>:][<Path>]<FileName1> <FileName2>
    % 文件名中有空格时，需要在路径外加""
    status = system(command); % 这个函数调用执行操作系统命令
    if status ~= 0
        disp([oldName{i}, '重命名失败。\n'])
    end
end