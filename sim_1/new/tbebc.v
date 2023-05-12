`timescale 1s / 1ns

module test_ecb_enc;

	reg [64:1] key;
	integer i;
	integer f;
	reg [64:1] msg[1:131072];
	reg [64:1] message;
	wire [64:1] enigma;

	ECB_enc e(enigma, message, key);
	initial 
	begin
		
		#5 $readmemb("D:/Aditya/Verilog/I CHIP/binary.txt",msg);
		f=$fopen("D:/Aditya/Verilog/I CHIP/Enigma.txt","w");
		#5
		for(i=1;i<=131072;i=i+1)
		 begin
			  #1 message=msg[i];
			  key = 64'b0001100011000000001000000000001100100000000010000010000000000011;
			  $display("%b",enigma);
			  $fwrite(f,"%b\n",enigma);
		 end 
		#10 $fclose(f);
	end
      
endmodule
