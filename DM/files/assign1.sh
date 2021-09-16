
bash case-generator.sh   
echo "executed case-generator.sh"

bash complete-vaccination-generator.sh  
echo "executed complete-vaccination-generator.sh"

bash edge-generator.sh                  
echo "executed edge-generator.sh"

bash peaks-generator.sh
echo "executed peaks-generator.sh"

bash vaccinated-count-generator.sh
echo "executed vaccinated-count-generator.sh"

bash vaccinated-ratio-generator.sh 
echo "executed vaccinated-ratio-generator.sh"

bash vaccination-population-ratio-generator.sh
echo "executed vaccination-population-ratio-generator.sh"

bash vaccine-type-ratio-generator.sh
echo "executed vaccine-type-ratio-generator.sh"

echo "Finished. Please check the 'output' directory for the resultant CSV files."