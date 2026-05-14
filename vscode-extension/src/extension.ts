import * as vscode from 'vscode';
import axios from 'axios';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {

    console.log('QA Architect AI activated');

    const disposable = vscode.commands.registerCommand(
        'qa-architect.generateFramework',
        async () => {

            const prompt = await vscode.window.showInputBox({
                placeHolder: 'Describe the QA framework to generate',
                prompt: 'Example: Generate Selenium Java enterprise framework'
            });

            if (!prompt) {
                return;
            }

            const workspaceFolders = vscode.workspace.workspaceFolders;

            if (!workspaceFolders || workspaceFolders.length === 0) {
                vscode.window.showErrorMessage(
                    'Please open a workspace folder first.'
                );
                return;
            }

            const config = vscode.workspace.getConfiguration('qaArchitect');

            const apiUrl = config.get<string>(
                'apiUrl',
                'http://127.0.0.1:8001'
            );

            const outputDirSetting = config.get<string>(
                'outputDir',
                'generated/test-framework'
            );

            const workspacePath = workspaceFolders[0].uri.fsPath;

            const outputDir = path.isAbsolute(outputDirSetting)
                ? outputDirSetting
                : path.join(workspacePath, outputDirSetting);

            try {

                await vscode.window.withProgress(
                    {
                        location: vscode.ProgressLocation.Notification,
                        title: 'Generating QA Framework...',
                        cancellable: false
                    },
                    async () => {

                        const response = await axios.post(
                            `${apiUrl}/generate`,
                            {
                                prompt,
                                output_dir: outputDir
                            },
                            {
                                timeout: 120000
                            }
                        );

                        console.log(response.data);
                    }
                );

                const openChoice = await vscode.window.showInformationMessage(
                    'Framework generated successfully!',
                    'Open Folder'
                );

                if (openChoice === 'Open Folder') {
                    vscode.commands.executeCommand(
                        'vscode.openFolder',
                        vscode.Uri.file(outputDir),
                        true
                    );
                }

            } catch (error: any) {

                const message =
                    error?.response?.data?.detail ||
                    error?.message ||
                    'Unknown error';

                vscode.window.showErrorMessage(
                    `Generation Failed: ${message}`
                );

                console.error(error);
            }
        }
    );

    context.subscriptions.push(disposable);
}

export function deactivate() {}



