import * as vscode from 'vscode';
import axios from 'axios';

export function activate(context: vscode.ExtensionContext) {

    console.log('QA Architect AI activated');

    const disposable = vscode.commands.registerCommand(
        'qa-architect.generateFramework',
        async () => {

            const prompt = await vscode.window.showInputBox({
                placeHolder: 'Describe the QA framework to generate'
            });

            if (!prompt) {
                return;
            }

            try {

                const response = await axios.post(
                    'http://127.0.0.1:8001/generate',
                    {
                        prompt,
                        output_dir: '/Users/varunmalhotra/Desktop/qa-architect/generated/test-framework'
                    }
                );

                vscode.window.showInformationMessage(
                    'Framework generated successfully!'
                );

                console.log(response.data);

            } catch (error: any) {

                vscode.window.showErrorMessage(
                    `Generation Failed: ${error.message}`
                );

                console.error(error);
            }
        }
    );

    context.subscriptions.push(disposable);
}

export function deactivate() {}


