from ipykernel.kernelbase import Kernel
import brainfuck

pointer = 0
cells = [0]

class BrainfuckKernel(Kernel):
    implementation = 'Brainfuck'
    implementation_version = '0.0'
    language = 'brainfuck'
    language_version = '0.1'
    language_info = {
        'name': 'brainfuck',
        'mimetype': 'text/plain',
        'file_extension': '.br',
    }
    banner = "Brainfuck kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        global pointer
        global cells
        if code == "flush":
            pointer = 0
            cells = [0]
        code, pointer, cells = brainfuck.process_string(code,pointer,cells)
        if not silent:
            stream_content = {'name': 'stdout', 'text': code}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=BrainfuckKernel)
else:
    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=BrainfuckKernel)
